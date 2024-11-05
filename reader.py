#DO NOT USE!

# import os.path

# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

# # If modifying these scopes, delete the file token.json.
# SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# # The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = "1MtFkgzpaieVug2dL_x-8489URvUHiwCPlnQ2KG1TlKU"
# SAMPLE_RANGE = "AAPL!A2:F125"

# def main():
#   """Shows basic usage of the Sheets API.
#   Prints values from a sample spreadsheet.
#   """
#   creds = None
#   # The file token.json stores the user's access and refresh tokens, and is
#   # created automatically when the authorization flow completes for the first
#   # time.
#   if os.path.exists("token.json"):
#     creds = Credentials.from_authorized_user_file("token.json", SCOPES)
#   # If there are no (valid) credentials available, let the user log in.
#   if not creds or not creds.valid:
#     if creds and creds.expired and creds.refresh_token:
#       creds.refresh(Request())
#     else:
#       flow = InstalledAppFlow.from_client_secrets_file(
#           "credentials.json", SCOPES
#       )
#       creds = flow.run_local_server(port=0)
#     # Save the credentials for the next run
#     with open("token.json", "w") as token:
#       token.write(creds.to_json())

#   try:
#     service = build("sheets", "v4", credentials=creds)

#     tickers = ["AAPL", "TSLA", "META", "PLTR", "NVDA"]

#     # Call the Sheets API
    

#     for ticker in tickers:
#       sample_range = ticker + "!A2:F125"
      
#       #print(sample_range)
#       sheet = service.spreadsheets()
#       result = (
#           sheet.values()
#           .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=sample_range)
#           .execute()
#       )
#       values = result.get("values", [])

#       if not values:
#         print("No data found.")
#         return
      
#       # print(values)
#       # Continue on from here:
#       dataframe = []
#       for row in values:
#         data = {"date":row[0], "open":float(row[1]), "close":float(row[4]), "high":float(row[2]), "low":float(row[3])}
#         dataframe.append(data)

#       result = signal_generator(dataframe)
#       print(ticker + " trending UP" if result else ticker + " trending DOWN")

#   except HttpError as err:
#     print(err)

# def signal_generator(df):
#   fifty_sma = 0
#   for frame in df[0:50]:
#     fifty_sma = fifty_sma + frame["close"]
#   fifty_sma = fifty_sma/50
#   hun_sma = 0
#   for frame in df[0:100]:
#     hun_sma = hun_sma + frame["close"]
#   hun_sma = hun_sma/100
  
#   return hun_sma < fifty_sma

# if __name__ == "__main__":
#   main()