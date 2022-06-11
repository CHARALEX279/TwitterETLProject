keywordWorkbook = "Windows:\\User\\Path\\Insert_Yours_Here.xslx"
csvFileName = "Insert_Yours_Here.csv"
bearerToken = "Insert_Yours_Here"
consumerKey = "Insert_Yours_Here"
consumerSecretKey = "Insert_Yours_Here"
accessToken = "Insert_Yours_Here"
secretToken = "Insert_Yours_Here"

#make a customized csv. Pandas is another automated option to make a csv
def makeNewCSV(csvFileName):
    csvFile = open(csvFileName, "a", newline = "", encoding = "utf-8")
    csvWriter = csvFile.writer(csvFile, delimiter = ",")

    csvWriter.writerow(["created_at", "tweet_id", "author_id", "user_name", "user_bio"])
    csvFile.close()
