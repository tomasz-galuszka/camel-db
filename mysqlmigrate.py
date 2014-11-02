import sys
from camel.CamelSchema import CamelSchema
import os
from camel.CamelBackup import CamelBackup
from camel.CamelUtils import CamelUtils
from camel.CamelTestSuite import CamelTestSuite

#changesetsDir = "changesets/"
camelSchema = CamelSchema()
camelUtils = CamelUtils()

args = sys.argv
if len(args) <= 1:
    print "Please input migrate | update [number] | backup | restore [backupFile] | test [schemaNumber] | shema"
else:
    command = args[1]
    
    if command == "schema":
        schemaNumber = camelSchema.getSchemaVersion()
        print " ----Current shema number: %s" % schemaNumber 
   
    if command == "migrate":
        camelSchema.executeChangesets(camelUtils.getConnectionParams()[4])
   
    if command == "update":
        if len(args) != 3:
            print " ----Incorrect schema number."
        else:
            newSchema = int(args[2])
            camelSchema.updateSchema(newSchema)
    
    if command == "test":
        if len(args) != 3:
            print " ----Incorrect schema number."
        else:
            CamelTestSuite().runTests(args[2])
         
    if command == "backup":
        camelBackup  = CamelBackup()
        camelBackup.backup()
    
    if command == "restore":
        if len(args) != 3:
            print "Please input existing backup file"
        else:
            if os.path.isfile(args[2]):
                print " ----Restore database from file : " + args[2]
                camelBackup  = CamelBackup()
                camelBackup.restore(args[2])
            else:
                print args[2]  + " is not a file."

camelSchema.disconnect()