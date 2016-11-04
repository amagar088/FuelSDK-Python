import ET_Client
from MarketingCloudSDK.client import ET_Client
from MarketingCloudSDK.objects import ET_CreateOptions, ET_DeleteOptions, ET_DataExtension
RequestType = "Asynchronous"
QueuePriority = "High" / "Medium" / "Low"
myClient = ET_Client()
try:
    debug = False
    stubObj = ET_Client.ET_Client(False, debug)
    
    ## Example using CreateDataExtensions() method

    # Declare a Python dict which contain all of the details for a DataExtension
    deOne = {"Name" : "HelperDEOne","CustomerKey" : "HelperDEOne"}
    deOne['columns'] = [{"Name" : "Name", "FieldType" : "Text", "IsPrimaryKey" : "true", "MaxLength" : "100", "IsRequired" : "true"},{"Name" : "OtherField", "FieldType" : "Text"}]
    
    # Declare a 2nd Python dict which contain all of the details for a DataExtension
    deTwo = {"Name" : "HelperDETwo","CustomerKey" : "HelperDETwo"}
    deTwo['columns'] = [{"Name" : "Name", "FieldType" : "Text", "IsPrimaryKey" : "true", "MaxLength" : "100", "IsRequired" : "true"},{"Name" : "OtherField", "FieldType" : "Text"}]
    
    # Call CreateDataExtensions passing in both DataExtension Hashes as an Array
    createDEResponse = stubObj.CreateDataExtensions([deOne, deTwo])
    print 'CreateDataExtensions Status: ' + str(createDEResponse.status)
    print 'Code: ' + str(createDEResponse.code)
    print 'Message: ' + str(createDEResponse.message)
    print 'Results Length: ' + str(len(createDEResponse.results))
    print 'Results: ' + str(createDEResponse.results)
    
    # Cleaning uprint the newly created DEs
    # Delete deOne
    print '>>> Delete deOne'
    de5 = ET_Client.ET_DataExtension()
    de5.auth_stub = stubObj
    de5.props = {"CustomerKey" : "HelperDEOne"}
    delResponse = de5.delete()
    print 'Delete Status: ' + str(delResponse.status)
    print 'Code: ' + str(delResponse.code)
    print 'Message: ' + str(delResponse.message)
    print 'Results: ' + str(delResponse.results)
    
    # Delete deTwo
    print '>>> Delete deTwo'
    de5 = ET_Client.ET_DataExtension()
    de5.auth_stub = stubObj
    de5.props = {"CustomerKey" : "HelperDETwo"}
    delResponse = de5.delete()
    print 'Delete Status: ' + str(delResponse.status)
    print 'Code: ' + str(delResponse.code)
    print 'Message: ' + str(delResponse.message)
    print 'Results: ' + str(delResponse.results)

    #Asynchronous Soap request to create multiple DataExtension, POST method

    #Explicitly passing the parameter , RequestType & QueuePriority
    createOptions = ET_CreateOptions(RequestType, QueuePriority)
    createOptions.auth_stub = myClient
    ## Example using CreateDataExtensions() method

    # Declare a Python dict which contain all of the details for a DataExtension
    deOne = {"Name": "HelperDEOne", "CustomerKey": "HelperDEOne"}
    deOne['columns'] = [{"Name" : "Name", "FieldType" : "Text", "IsPrimaryKey" : "true", "MaxLength" : "100", "IsRequired" : "true"},{"Name" : "OtherField", "FieldType" : "Text"}]

    # Declare a 2nd Python dict which contain all of the details for a DataExtension
    deTwo = {"Name": "HelperDETwo", "CustomerKey": "HelperDETwo"}
    deTwo['columns'] = [{"Name": "Name", "FieldType": "Text", "IsPrimaryKey": "true", "MaxLength": "100", "IsRequired": "true"}, {"Name": "OtherField", "FieldType": "Text"}]

    createDEResponse = myClient.CreateDataExtensions([deOne, deTwo], createOptions)
    print 'CreateDataExtensions Status: ' + str(createDEResponse.status)
    print 'Code: ' + str(createDEResponse.code)
    print 'Message: ' + str(createDEResponse.message)
    print 'Results Length: ' + str(len(createDEResponse.results))
    print 'Results: ' + str(createDEResponse.results)

    #Asynchronous Soap request to delete DataExtensions, Delete method

    #Explicitly passing the parameter, RequestType & QueuePriority
    deleteDEOne = ET_DeleteOptions(RequestType, QueuePriority)
    deleteDEOne.auth_stub = myClient
    # Cleaning uprint the newly created DEs
    # Delete deOne
    print '>>> Delete deOne'
    de5 = ET_DataExtension()
    de5.auth_stub = myClient
    de5.props = {"CustomerKey": "HelperDEOne"}
    de5.delOptions = deleteDEOne
    delResponse = de5.delete()
    print 'Delete Status: ' + str(delResponse.status)
    print 'Code: ' + str(delResponse.code)
    print 'Message: ' + str(delResponse.message)
    print 'Results: ' + str(delResponse.results)

    # Delete deTwo
    print '>>> Delete deTwo'
    delet2DE = ET_DeleteOptions(RequestType, QueuePriority)
    delet2DE.auth_stub = myClient
    de5 = ET_DataExtension()
    de5.auth_stub = myClient
    de5.props = {"CustomerKey": "HelperDETwo"}
    de5.delOptions = delet2DE
    delResponse = de5.delete()
    print 'Delete Status: ' + str(delResponse.status)
    print 'Code: ' + str(delResponse.code)
    print 'Message: ' + str(delResponse.message)
    print 'Results: ' + str(delResponse.results)


except Exception as e:
    print 'Caught exception: ' + e.message
    print e