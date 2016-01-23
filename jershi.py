import requests

"""
For the examples we are using 'requests' which is a popular minimalistic python library for making HTTP requests.
Please use 'pip install requests' to add it to your python libraries.
"""

em_etfs= ["EPHE", "EWM", "TLTE", "HEEM", "ERUS", "PIE", "BKF", "SCIF", "GMM", "DVYE", "EELV", "BBRC", "EPOL", "DBEM", "ADRE", "FEM", "IDX",
"EEMS", "EMFM", "QEMM", "EEB", "BIK", "SMIN", "AFK", "QAT", "VWO", "EEM", "IEMG", "INDA", "EEMV", "RSX", "EPI", "SCHE", "DEM", "DGS", "INDY",
"GEM", "FM", "PIN", "VNM", "FNDE", "EWX", "AIA", "TUR", "PXH", "EIDO", "INP", "EZA", "EDIV", "THD", "DGRE", "FRN", "GUR", "JPEM", "RSXJ",
"GAF", "UAE", "GULF", "EGPT", "SCIN", "FEMS", "RBL", "ROAM", "NGE", "HILO", "PLND", "EMDD", "EMCG", "ASEA", "EMQQ", "EWEM", "BICK", "EDOG",
"MES", "IDXJ", "PAK", "QEM", "EMCR", "QDEM", "KSA", "EMFT", "KLEM", "EMGF", "SDEM", "AZIA", "EMSD", "TLEH", "EMBB", "HDEE", "KEMP", "XSOE",
"EEHB", "XCEM", "HEMV"]

portfolioAnalysisRequest = requests.get("https://test3.blackrock.com/tools/hackathon/security-data",
	params= {'identifiers':em_etfs})
print(portfolioAnalysisRequest.text) # get in text string format
# portfolioAnalysisRequest.json # get as json object