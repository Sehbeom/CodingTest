def solution(id_list, report, k):
    answer=[0]*len(id_list)
    reportNum = [0]*len(id_list)
    reportInfo = {}
    restrictedUser = []
    
    for oneReport in report:
        reportedId = oneReport.split(" ")
        
        if reportedId[0] in reportInfo:
            if (reportedId[1] in reportInfo[reportedId[0]]) == False:
                reportInfo[reportedId[0]].append(reportedId[1])
        else:
            reportedArray = [reportedId[1]]*1
            reportInfo[reportedId[0]] = reportedArray
    
    for oneReportInfo in reportInfo:
        for reportedPerUser in reportInfo[oneReportInfo]:
            if reportedPerUser in restrictedUser:
                continue
            else:
                reportNum[id_list.index(reportedPerUser)]+=1
                if reportNum[id_list.index(reportedPerUser)]>=k:
                    restrictedUser.append(reportedPerUser)        
    
    for i in range(0,len(id_list)):
        if id_list[i] in reportInfo:
            for a in reportInfo[id_list[i]]:
                if a in restrictedUser:
                    answer[i]+=1
    
    return answer