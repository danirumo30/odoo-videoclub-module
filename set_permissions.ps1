# Requires -Version 5.1
###############################################################################
# @author https://github.com/javnitram/
# GNU GENERAL PUBLIC LICENSE Version 3
# Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
###############################################################################

$ErrorActionPreference = "Stop"

# VARIABLES GLOBALES
# Los nombres en SERVICES deben coincidir con los nombres de directorios en la
# ruta actual y con los servicios definidos en el fichero docker-compose.yml
$SERVICES = @('odoo', 'pgadmin4')
$RED_TEXT = "`e[0;31m"
$GREEN_TEXT = "`e[0;32m"
$RESET_TEXT = "`e[0m"

function Get-UserID {
    $id = [System.Security.Principal.WindowsIdentity]::GetCurrent().User.Value
    return $id
}

function Get-GroupID {
    $id = [System.Security.Principal.WindowsIdentity]::GetCurrent().Groups[0].Value
    return $id
}

function Set-PermissionsForContainers {
    foreach ($i in $SERVICES) {
        $container_ids = docker ps --quiet --filter "name=^$i"
        foreach ($container_id in $container_ids) {
            $mounts = Select-String -Path "docker-compose.yml" -Pattern "./$i" | ForEach-Object { $_.Line.Split(':')[1] }
            foreach ($mount in $mounts) {
                Write-Output "Estableciendo permisos en el contenedor con id $container_id basado en la imagen $i, punto de montaje $mount"
                docker exec --privileged --user root $container_id sh -c "/usr/bin/find $mount -type d -exec /bin/chmod 777 {} \;"
                docker exec --privileged --user root $container_id sh -c "/usr/bin/find $mount -type f -exec /bin/chmod 666 {} \;"
                $user_id = Get-UserID
                $group_id = Get-GroupID
                docker exec --privileged --user root $container_id sh -c "/bin/chown -R ${user_id}:${group_id} $mount"
            }
        }
    }
}

function Set-PermissionsForHost {
    $error = $false
    foreach ($i in $SERVICES) {
        try {
            New-Item -Path $i -ItemType Directory -Force
            Get-ChildItem -Path $i -Recurse -Directory | ForEach-Object { $_.Attributes = 'ReadOnly' }
            Get-ChildItem -Path $i -Recurse -File | ForEach-Object { $_.Attributes = 'ReadOnly' }
        }
        catch {
            $error = $true
        }
    }

    if ($error) {
        Write-Output "${RED_TEXT}"
        Write-Error "Ha habido problemas al asignar algunos permisos de directorios locales. Entre otras cosas, puede afectar a:
        - La correcta ejecución de los contenedores y persistencia de sus datos.
        - La correcta migración de los ficheros usados en los puntos de montaje a otros entornos.

    Si los contenedores están en ejecución, vuelve a lanzar `"$0`" tras hacer `docker-compose down`.
    Si no, vuelve a lanzar `"$0`" tras hacer `docker-compose up -d`."
        Write-Output "${RESET_TEXT}"
        Exit 1
    }
    else {
        Write-Output "Permisos locales asignados correctamente.`n"
    }
}

# Esta funcion gestiona permisos de los bind mounts, almacenamiento basado el montaje 
# de ficheros o directorios del anfitrión en el contenedor.
# Los bind mounts dependen del sistema ficheros subyacente y pueden dañar el sistema anfitrión. 
# Se recomienda usar volúmenes gestionados por Docker para hacer persistentes los datos de los
# contenedores, los bind mount son apropiados para compartir ficheros de configuración y código,
# como es el caso de este proyecto.
# @see https://docs.docker.com/storage/bind-mounts/
#      https://docs.docker.com/storage/#good-use-cases-for-bind-mounts
function Set-Permissions {
    (Get-Item -Path ".").Attributes = 'ReadOnly'
    Set-PermissionsForContainers
    Set-PermissionsForHost
}

if ($PSCommandPath -eq $MyInvocation.MyCommand.Path) {
    # Están ejecutando directamente este script, no importándolo con source
    Set-Permissions
}