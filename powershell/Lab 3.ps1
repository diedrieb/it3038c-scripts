function GetIP {
   (get-netipaddress).ipv4address | Select-String "192*"
}

function GetUser {
    whoami
} 

function GetHostname {
    hostname
}

function Version {
    $PSVersionTable.PSVersion
}

function TodayDate {
    Get-Date -Format "dddd MM/dd/yyyy"
}

$IP = GetIP
$USER = GetUser
$HOSTNAME = GetHostname
$VERSION = Version 
$DATE = TodayDate

Write-Host("This machine's IP is $IP. User is $USER. Hostname is $HOSTNAME. Powershell Version $VERSION. Today's date is $DATE.")
