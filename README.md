SETTING UP DOCKER:
    run "docker compose up"
    Possible errors:
        -org.apache.zookeeper.KeeperException$NodeExistsException: KeeperErrorCode = NodeExists
            Trying after a minute or pulling images again seems to solve the issue.
            Also as soon as running docker up command, "sudo docker exec -it databoss-kafka-1 rm -f ./logs" can be run too

CONNECTING DATABASES:
    The tables should have at least one serial column to work properly.
    The table configuration should be done on the tables.json file
    Example configuration can be found at example.json
    After configuring the json, "python3 parse_tables.py" should be run

    
