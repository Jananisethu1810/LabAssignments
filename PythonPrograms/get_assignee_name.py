import pandas

'''
This function is used for finding all the assignee names for the given assignment group and the summary
'''
def find_assignee_name(assignment_group, summary):
    assignee=[]
    criteria_both=findersheet.loc[
        (findersheet['Assignment Group']==assignment_group) &
        (findersheet['Selection Criteria']=='Both'),
        ['Unique keywords', 'Cluster', 'Assignee Name', 'SPOC Name']];
    #print(criteria_both)

    criteria_cluster=findersheet.loc[
        (findersheet['Assignment Group']==assignment_group) &
        (findersheet['Selection Criteria']=='CLUSTER'),
        ['Unique keywords', 'Cluster', 'Assignee Name', 'SPOC Name']];
    #print(criteria_cluster)

    criteria_keyword=findersheet.loc[
        (findersheet['Assignment Group']==assignment_group) &
        (findersheet['Selection Criteria']=='KEYWORD'),
        ['Unique keywords', 'Cluster', 'Assignee Name', 'SPOC Name']];
    flag=0

    if(criteria_both.shape[0]>0 and flag==0):
        for index, row in criteria_both.iterrows():
            if(str(row['Unique keywords']).upper() in summary.upper() and str(row['Cluster']).upper() in summary.upper()):
                #print(index)
                assignee=str(row['Assignee Name'])
                flag=1
                break
    if(criteria_cluster.shape[0]>0 and flag==0):
        for index, row in criteria_cluster.iterrows():
            if(str(row['Cluster']).upper() in summary.upper()):
                #print(index)
                assignee=str(row['Assignee Name'])
                flag=1
                break
    if(criteria_keyword.shape[0]>0 and flag==0):
        for index, row in criteria_keyword.iterrows():
            if(str(row['Unique keywords']).upper() in summary.upper()):
                #print(index)
                assignee=str(row['Assignee Name'])
                flag=1
                break;
    return assignee
'''
This function is used for finding the availble assignee from the list of assignees
'''
def find_availability(assignees_list):
    available_assignee=[]
    name_availability=availability.loc[:,['Resource Name', 'Availability']]
    spoc_name=findersheet.loc[:,['Assignee Name', 'SPOC Name']]
    available=0;
    if(name_availability.shape[0]>0):
        for index, row in name_availability.iterrows():
            if(str(row['Resource Name']).upper() in assignees_list.upper() and str(row['Availability'])=='Yes'):
                #print(index)
                available_assignee=str(row['Resource Name'])
                available=1;
                break;
    if available==0:
        for index, row in spoc_name.iterrows():
            if(str(row['Assignee Name']).upper() in assignees_list.upper()):
                #print(index)
                available_assignee=str(row['SPOC Name']);
                break;
            
    return available_assignee;        

findersheet=pandas.read_excel(r'C:\Users\jananis\Downloads\AssigneeDetails.xlsx', sheet_name='Finder');
availability=pandas.read_excel(r'C:\Users\jananis\Downloads\AssigneeDetails.xlsx', sheet_name='Availability');
assignment_group='CAPGEM_DCX_EDI_WW_L2'
summary="UK"
assignees=find_assignee_name(assignment_group, summary)
print(assignees);
print(find_availability(assignees));



                                 
