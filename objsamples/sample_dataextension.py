import ET_Client
from MarketingCloudSDK.objects import ET_CreateOptions, ET_UpdateOptions, ET_DataExtension_Row, ET_DataExtension, ET_DeleteOptions
from MarketingCloudSDK.client import ET_Client
myClient = ET_Client()
try:
    debug = False
    stubObj = ET_Client.ET_Client(False, debug)

    RequestType = "Asynchronous"
    QueuePriority = "High" / "Medium" / "Low"

    # Get all of the DataExtensions in an Account
    print '>>> Get all of the DataExtensions in an Account'
    de = ET_Client.ET_DataExtension()
    de.auth_stub = stubObj
    de.props = ["CustomerKey", "Name"]
    getResponse = de.get()
    print 'Retrieve Status: ' + str(getResponse.status)
    print 'Code: ' + str(getResponse.code)
    print 'Message: ' + str(getResponse.message)
    print 'MoreResults: ' + str(getResponse.more_results)
    print 'RequestID: ' + str(getResponse.request_id)
    print 'Results Length: ' + str(len(getResponse.results))
    #print 'Results: ' + str(getResponse.results)

    # Get all of the DataExtensions in an Account belonging to a specific sub account
    print '>>> Get all of the DataExtensions in an Account belonging to a specific sub account'
    de = ET_Client.ET_DataExtension()
    de.auth_stub = stubObj
    de.props = ["CustomerKey", "Name"]
    de.options = {"Client": {"ID": "1234567"}}
    getResponse = de.get()
    print 'Retrieve Status: ' + str(getResponse.status)
    print 'Code: ' + str(getResponse.code)
    print 'Message: ' + str(getResponse.message)
    print 'MoreResults: ' + str(getResponse.more_results)
    print 'RequestID: ' + str(getResponse.request_id)
    print 'Results Length: ' + str(len(getResponse.results))
    #print 'Results: ' + str(getResponse.results)

    # Specify a name for the data extension that will be used for testing
    # Note: Name and CustomerKey will be the same value
    # WARNING: Data Extension will be deleted so don't use the name of a
    # production data extension
    NameOfDE = "ThisWillBeDeleted-Test"


    # Create  Data Extension
    print '>>> Create Data Extension'
    de2 = ET_Client.ET_DataExtension()
    de2.auth_stub = stubObj
    de2.props = {"Name" : NameOfDE,"CustomerKey" : NameOfDE}
    de2.columns = [{"Name" : "Name", "FieldType" : "Text", "IsPrimaryKey" : "true", "MaxLength" : "100", "IsRequired" : "true"},{"Name" : "OtherField", "FieldType" : "Text"}]
    postResponse = de2.post()
    print 'Post Status: ' + str(postResponse.status)
    print 'Code: ' + str(postResponse.code)
    print 'Message: ' + str(postResponse.message)
    print 'Results: ' + str(postResponse.results)
    # Update DE to add new field
    print '>>> Update DE to add new field'
    de3 = ET_Client.ET_DataExtension()
    de3.auth_stub = stubObj
    de3.props = {"Name" : NameOfDE,"CustomerKey" : NameOfDE}
    de3.columns = [{"Name" : "AddedField", "FieldType" : "Text"}]
    patchResponse = de3.patch()
    print 'Patch Status: ' + str(patchResponse.status)
    print 'Code: ' + str(patchResponse.code)
    print 'Message: ' + str(patchResponse.message)
    print 'Results: ' + str(patchResponse.results)



    # Retrieve all columns for data extension
    print '>>> Retrieve all columns for data extension '
    myDEColumn = ET_Client.ET_DataExtension_Column()
    myDEColumn.auth_stub = stubObj
    myDEColumn.props = ["Name"]
    myDEColumn.search_filter = {'Property' : 'CustomerKey','SimpleOperator' : 'equals','Value' : NameOfDE}
    getResponse = myDEColumn.get()
    print 'Retrieve Status: ' + str(getResponse.status)
    print 'Code: ' + str(getResponse.code)
    print 'Message: ' + str(getResponse.message)
    print 'MoreResults: ' + str(getResponse.more_results)
    print 'RequestID: ' + str(getResponse.request_id)
    print 'Results Length: ' + str(len(getResponse.results))
    print 'Results: ' + str(getResponse.results)


    # Add a row to a data extension (using CustomerKey)
    print '>>>  Add a row to a data extension'
    de4 = ET_Client.ET_DataExtension_Row()
    de4.CustomerKey = NameOfDE;
    de4.auth_stub = stubObj
    de4.props = {"Name" : "MAC3", "OtherField" : "Text3"}
    postResponse = de4.post()
    print 'Post Status: ' + str(postResponse.status)
    print 'Code: ' + str(postResponse.code)
    print 'Message: ' + str(postResponse.message)
    print 'Results: ' + str(postResponse.results)

    # Add a row to a data extension (Using Name)
    print '>>> Add a row to a data extension'
    de4 = ET_Client.ET_DataExtension_Row()
    de4.auth_stub = stubObj
    de4.Name = NameOfDE
    de4.props = {"Name" : "MAC4", "OtherField" : "Text3"}
    postResponse = de4.post()
    print 'Post Status: ' + str(postResponse.status)
    print 'Code: ' + str(postResponse.code)
    print 'Message: ' + str(postResponse.message)
    print 'Results: ' + str(postResponse.results)

    # Retrieve all rows
    print '>>> Retrieve all rows'
    row = ET_Client.ET_DataExtension_Row()
    row.auth_stub = stubObj
    row.CustomerKey = NameOfDE
    row.props = ["Name","OtherField"]
    getResponse = row.get()
    print 'Retrieve Status: ' + str(getResponse.status)
    print 'Code: ' + str(getResponse.code)
    print 'Message: ' + str(getResponse.message)
    print 'MoreResults: ' + str(getResponse.more_results)
    print 'RequestID: ' + str(getResponse.request_id)
    print 'Results Length: ' + str(len(getResponse.results))
    print 'Results: ' + str(getResponse.results)

    # Update a row in  a data extension
    print '>>> Update a row in  a data extension'
    de4 = ET_Client.ET_DataExtension_Row()
    de4.auth_stub = stubObj
    de4.CustomerKey = NameOfDE
    de4.props = {"Name" : "MAC3", "OtherField" : "UPDATED!"}
    postResponse = de4.patch()
    print 'Patch Status: ' + str(postResponse.status)
    print 'Code: ' + str(postResponse.code)
    print 'Message: ' + str(postResponse.message)
    print 'Results: ' + str(postResponse.results)

    # Retrieve only updated row
    print '>>> Retrieve only updated row'
    row = ET_Client.ET_DataExtension_Row()
    row.auth_stub = stubObj
    row.CustomerKey = NameOfDE
    row.props = ["Name","OtherField"]
    row.search_filter = {'Property' : 'Name','SimpleOperator' : 'equals','Value' : 'MAC3'}
    getResponse = row.get()
    print 'Retrieve Status: ' + str(getResponse.status)
    print 'Code: ' + str(getResponse.code)
    print 'Message: ' + str(getResponse.message)
    print 'MoreResults: ' + str(getResponse.more_results)
    print 'RequestID: ' + str(getResponse.request_id)
    print 'Results Length: ' + str(len(getResponse.results))
    print 'Results: ' + str(getResponse.results)

    # Delete a row from a data extension
    print '>>> Delete a row from a data extension'
    de4 = ET_Client.ET_DataExtension_Row()
    de4.auth_stub = stubObj
    de4.CustomerKey = NameOfDE
    de4.props = {"Name" : "MAC3"}
    deleteResponse = de4.delete()
    print 'Delete Status: ' + str(deleteResponse.status)
    print 'Code: ' + str(deleteResponse.code)
    print 'Message: ' + str(deleteResponse.message)
    print 'Results: ' + str(deleteResponse.results)

    # Delete a Data Extension
    print '>>> Delete a  Data Extension'
    de5 = ET_Client.ET_DataExtension()
    de5.auth_stub = stubObj
    de5.props = {"Name" : NameOfDE,"CustomerKey" : NameOfDE}
    delResponse = de5.delete()
    print 'Delete Status: ' + str(delResponse.status)
    print 'Code: ' + str(delResponse.code)
    print 'Message: ' + str(delResponse.message)
    print 'Results: ' + str(delResponse.results)


    # Retrieve lots of rows with moreResults
    print '>>> Retrieve lots of rows with moreResults'
    row = ET_Client.ET_DataExtension_Row()
    row.auth_stub = stubObj
    row.Name = "zipstolong"
    row.props = ["zip","latitude","longitude"]
    getResponse = row.get()
    print 'Retrieve Status: ' + str(getResponse.status)
    print 'Code: ' + str(getResponse.code)
    print 'Message: ' + str(getResponse.message)
    print 'MoreResults: ' + str(getResponse.more_results)
    print 'RequestID: ' + str(getResponse.request_id)
    print 'Results Length: ' + str(len(getResponse.results))
    #print 'Results: ' + str(getResponse.results)

    while getResponse.more_results: 
        print '>>> Continue Retrieve lots of rows with moreResults'
        getResponse = row.getMoreResults()
        print 'Retrieve Status: ' + str(getResponse.status)
        print 'Code: ' + str(getResponse.code)
        print 'Message: ' + str(getResponse.message)
        print 'MoreResults: ' + str(getResponse.more_results)
        print 'RequestID: ' + str(getResponse.request_id)
        print 'Results Length: ' + str(len(getResponse.results))

    #Asynchronous Soap request to create DataExtension, POST method
    #############################################################

    #Explicitly passing the parameter, RequestType & QueuePriority
    createOptions = ET_CreateOptions(RequestType, QueuePriority)
    createOptions.auth_stub = myClient
    dataExtension = ET_DataExtension()
    dataExtension.auth_stub = myClient
    dataExtension.props = {"Name": NameOfDE, "CustomerKey": NameOfDE}
    dataExtension.columns = [{"Name" : "Name", "FieldType" : "Text", "IsPrimaryKey" : "true", "MaxLength" : "100", "IsRequired" : "true"},{"Name" : "OtherField", "FieldType" : "Text"}]
    dataExtension.createOptions = createOptions
    results = dataExtension.post()
    print 'Post Status: ' + str(results.status)
    print 'Code: ' + str(results.code)
    print 'Message: ' + str(results.message)
    print 'Results: ' + str(results.results)

    #Asynchronous Soap request to delete DataExtension, Delete method
    #################################################################

    #Explicitly passing the parameter, RequestType & QueuePriority
    deleteDataExtension = ET_DeleteOptions(RequestType, QueuePriority)
    deleteDataExtension.auth_stub = myClient
    dataExtension = ET_DataExtension()
    dataExtension.auth_stub = myClient
    dataExtension.props = {"CustomerKey": "DataExtension_1"}
    dataExtension.delOptions = deleteDataExtension
    results = dataExtension.delete()
    print 'Delete Status: ' + str(results.status)
    print 'Code: ' + str(results.code)
    print 'Message: ' + str(results.message)
    print 'Results: ' + str(results.results)

    # Asynchronous Soap request to add a row , DataExtensionRow POST
    ################################################################

    dataExtensionRow = ET_DataExtension_Row()
    # Explicitly passing the parameter, RequestType and QueuePriority
    createOptions = ET_CreateOptions(RequestType, QueuePriority)
    createOptions.auth_stub = stubObj
    dataExtensionRow.auth_stub = stubObj
    dataExtensionRow.CustomerKey = "CustomerKey"
    dataExtensionRow.props = {"Field_1" : "Value_1", "Field_2" : "Value_2", "Field_3" : "Value_3"}
    dataExtensionRow.createOptions = createOptions
    results = dataExtensionRow.post()
    print 'Post Status: ' + str(results.status)
    print 'Code: ' + str(results.code)
    print 'Message: ' + str(results.message)
    print 'Results: ' + str(results.results)

    # Asynchronous Soap request to update arow in DataExtensionRow, PATCH method
    ############################################################################

    dataExtensionRow = ET_DataExtension_Row()
    # Explicitly passing the parameter, RequestType and QueuePriority
    updateOptions = ET_UpdateOptions(RequestType, QueuePriority)
    updateOptions.auth_stub = stubObj
    dataExtensionRow.auth_stub = stubObj
    dataExtensionRow.CustomerKey = "CustomerKey"
    #To Update a row first property must be a primary key, primary key name and value must be same as in DataExtension
    dataExtensionRow.props = {"PrimaryKeyName": "key_Value", "Field_1": "Updated_Value_1", "Field_2": "Updated_Value_2"}
    dataExtensionRow.updateOptions = updateOptions
    results = dataExtensionRow.patch()
    print 'Patch Status: ' + str(results.status)
    print 'Code: ' + str(results.code)
    print 'Message: ' + str(results.message)
    print 'Results: ' + str(results.results)

    #Asynchronous Soap request to delete a row, DataExtensionRow Delete method
    ###################################################################

    #Explicitly passing the parameter, RequestType & QueuePriority
    deleteOptions = ET_DeleteOptions(RequestType, QueuePriority)
    dataExtensionRow = ET_DataExtension_Row()
    deleteOptions.auth_stub = myClient
    dataExtensionRow.auth_stub = myClient
    dataExtensionRow.CustomerKey = "CustomerKey"
    # Here, Doing a delete and the props value must be a primary key.
    # Value for this key must not be changed
    dataExtensionRow.props = {"PrimaryKeyName": "key_Value"}
    dataExtensionRow.delOptions = deleteOptions
    results = dataExtensionRow.delete()
    print 'Delete Status: ' + str(results.status)
    print 'Code: ' + str(results.code)
    print 'Message: ' + str(results.message)
    print 'Results: ' + str(results.results)

except Exception as e:
    print 'Caught exception: ' + str(e.message)
    print e
