$scriptPath = "E:\Github\webserver_for_system_infos\app.py"
$envName = "webserver_for_system_info"

Set-Location "E:\Github\webserver_for_system_infos"
conda activate $envName
python $scriptPath
