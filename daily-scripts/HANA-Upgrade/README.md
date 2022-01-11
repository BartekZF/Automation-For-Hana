####### TO DO #######

### [+] 1. Backup! --> preconfig.yml

### TWO OPTIONS:

        a) User is providing the path where backup is stored, script is only checking if exist.
        b) Script will make an backup.

### [+] 2. Check if files are existing in provided path --> preconfig.yml

### THREE OPTIONS:

        a) User will provide path for SAR file. Script will have to use sapcar and then unzip file.
        b) User will provide path for ZIP file. Script will have to unzip the file.
        c) User will provide path for "ready-to-go" folder. Script will only check if necessary files are existing there (HDB_SERVER_LINUX_X64_ARM or HDB_LCM_LINUX, hdblcm ... etc.) [I WILL GO WITH THIS OPTION] ---> Agreeded at team meeting!

### [+] 3. Copy configfile from Git to OS level. --> configfile_template.yml // take ec2 instances tags of SID etc. {What for?}

### [+] 4. Shutdown SAP. --> stop_SAP.yml

### [+] 5. Execute installation. --> upgrade_hana.yml

### [-] 6. Post Upgrade Tasks --> post_upgrade.yml

### [+] 7. Start SAP. --> start_SAP.yml

####### LIST OF VARIABLES #######

        a) BACKUP_PATH -> Path were backup is stored {Required to execute AWX template}
        b) HANA_SRC_PATH -> Checking if exist, using to execute update script
        c) INST_NR -> HANA instance ID
        d) configfile.j2 variables:
                - components
                - sid
                - hostname
                - Passwords for SYSTEM user
                - Env Type {PROD, DEV, TEST, CUSTOM}

### IDEAS

1.  SYSTEM user unlocked >> Instead of checking, we can execute the backup script using SYSTEM user it will make two thing 1) Check if SYSTEM user is unlocked. 2) It will make backup in more automatic way.

        ###
        Command to use:
                - hdbsql -i {{INST_NR}} -u SYSTEM -p {{SYS_USER_PASSWORD}} -d SYSTEMDB "BACKUP DATA USING FILE ('{{BACKUP_PATH}}COMPLETE_DATA_BACKUP_SYSTEMDB_$(date '+%Y.%m.%d-%H:%M:%S')')"
                - hdbsql -i {{INST_NR}} -u SYSTEM -p {{SYS_USER_PASSWORD}} -d <SID_TENANT> "BACKUP DATA USING FILE ('{{BACKUP_PATH}}COMPLETE_DATA_BACKUP_TENANT_$(date '+%Y.%m.%d-%H:%M:%S')')"

        ###

2.  Disk free space
3.  Create yml for reading tags/variables
