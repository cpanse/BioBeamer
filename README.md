# Collecting instrument data using BioBeamer

[![Project Stats](https://www.openhub.net/p/BioBeamer/widgets/project_thin_badge.gif)](https://www.openhub.net/p/BioBeamer)


## Install 
* ensure you have python 2.7.* (for branch biobeamer2)
* ensure you have python 3.7 or higher (for branch p37).
* ```git clone git@github.com:fgcz/BioBeamer.git```
* if you want to use the p37 branch execute ```git checkout p37```

## Configure 

### BioBeamer xml configuration file

The entire file can be found here [Biobeamer.xml](biobeamer2/BioBeamer2.xml)


```xml

<?xml-stylesheet type="text/xsl" href="BioBeamer.xsl"?>
<BioBeamerHosts>
<host name="fgcz-i-180" 
    instrument="TRIPLETOF_1"
    min_size="1024" 
    min_time_diff="10800" 
    max_time_diff="2419200" 
    simulate='false' 
    func_target_mapping="map_data_analyst_tripletof1" 
    robocopy_args="/E /Z /NP /R:0 /LOG+:C:\\Progra~1\\BioBeamer\\robocopy.log"
    pattern=".+" 
    source_path="D:/Analyst Data/Projects/" 
    target_path="\\130.60.81.21\\Data2San">
    <b-fabric>
        <applicationID>93</applicationID>
    </b-fabric>
</host>
</BioBeamerHosts>

```

the xml can be validated using

```bash
xmllint --noout --schema BioBeamer.xsd BioBeamer.xml
```

or 

```bash
xmlstarlet val --xsd BioBeamer.xsd BioBeamer.xml
```

### Deploy @ new location
* change syslog host
* change configuration url

### Configure Syslog '/etc/rsyslog.conf' 

```syslog
$template tplremote,"%timegenerated% %HOSTNAME% %fromhost-ip% %syslogtag%%msg:::drop-last-lf%\n"
$template RemoteHost,"/var/log/remote/%HOSTNAME%_%fromhost-ip%.log"

if ($fromhost-ip != '127.0.0.1') then ?RemoteHost;tplremote  
& ~
```

### Configure logrotate '/etc/logrotate.d/remote'
```conf
/var/log/remote/*
{
        rotate 13
        monthly
        missingok
        notifempty
        compress
}
```

## Run

### @ FGCZ
just 'run as administrator' justBeamFiles.exe.

justBeamFiles.exe is an [autoitscript](https://www.autoitscript.com/site/autoit/).
In our case the justBeamFiles.exe maps the storage and runs the fgcz_biobeamer.py script which uses robocopy.exe on Micorsoft installed PCs to sync the files.

### otherwise
* ensure that SAN is mounted 
```cmd
python BioBeamer.py
```

## BioBeamer class
![BioBeamer UML](/images/classes_No_Name.png)


## Author
[Christian Panse](http://www.fgcz.ch/the-center/people/panse.html) :rocket:

## See also
* [fgcz-intranet wiki page](http://fgcz-intranet.uzh.ch/tiki-index.php?page=BioBeamer)
* [FGCZ configuration](http://fgcz-data.uzh.ch/config/BioBeamer.xml)

## TODO
* munin plugin

