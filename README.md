SETTING UP DOCKER:<br>
&nbsp;&nbsp;&nbsp;&nbsp; run "docker compose up"<br>
&nbsp;&nbsp;&nbsp;&nbsp;Possible errors: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-org.apache.zookeeper.KeeperException$NodeExistsException: KeeperErrorCode = NodeExists <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Trying after a minute or pulling images again seems to solve the issue. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Also as soon as running docker up command, "sudo docker exec -it databoss-kafka-1 rm -f ./logs" can be run too
<br><br>
CONNECTING DATABASES:<br>
&nbsp;&nbsp;&nbsp;&nbsp;The tables should have at least one serial column or one timestamp column to work properly. <br>
&nbsp;&nbsp;&nbsp;&nbsp;The timestamp column should be non-nullable. <br>
&nbsp;&nbsp;&nbsp;&nbsp;Only newly added rows which timestamps or serials are bigger than the previous biggest are added to new table. <br>
&nbsp;&nbsp;&nbsp;&nbsp;The table configuration should be done on the tables.json file <br>
&nbsp;&nbsp;&nbsp;&nbsp;Example configuration can be found at example.json <br>
&nbsp;&nbsp;&nbsp;&nbsp;After configuring the json, "python3 parse_tables.py" should be run <br>

    
