Write-Host Hello World

$CPartition=Get-Volume -DriveLetter C 

$Prozenz=($CPartition.SizeRemaining/$CPartition.Size)*100 

if($Prozenz -lt 20) 

{ 
    Write-Host Es sind weniger als 20% Speicherplatz verfuegbar.
    Write-Host Freier Speicherplatz: $Prozenz%
} 
else 
{ 
    Write-Host Es ist genug Speicherplatz verfuegbar.
    Write-Host Freier Speicherplatz: $Prozenz%
}

$WindowsProzesse=Get-Process 

foreach($Prozess in $WindowsProzesse) 
{ 
    Write-Host $Prozess.Name 
}


#$i=1; 

#for($i;$i -le 10;$i++) 

#{ 
 #   $Ordnername="Ordner$i"
    #New-Item -ItemType Directory -Path "C:\Temp" -Name $Ordnername 
#}

[void][Reflection.Assembly]::LoadWithPartialName('Microsoft.VisualBasic')

$title = 'Demographics'
$msg   = 'Enter your demographics:'

$text = [Microsoft.VisualBasic.Interaction]::InputBox($msg, $title)

Write-Host $text