from google_images_download import google_images_download

# download images of star trek species
response = google_images_download.googleimagesdownload()

arguments = {"keywords":"star trek cardassian,star trek klingon,star trek ferengi,star trek vulcan, star trek andorian","limit":100,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images

