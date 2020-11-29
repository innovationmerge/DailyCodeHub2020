# iNNovationMerge

# Python program to extract metadata from tiff and jpeg files

# pip install ExifRead
import exifread
inputPath = "ImageFile.jpg"
# Open image file for reading (binary mode)
f = open(inputPath, 'rb')

# Return Exif tags
tags = exifread.process_file(f)
for tag in tags.keys():
    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
        print("%s : %s" % (tag, tags[tag]))

# ExifRead Tags output
"""
Image Make : , Nokia
Image Model : , 5230
Image Orientation : , Horizontal (normal)
Image XResolution : , 300
Image YResolution : , 300
Image ResolutionUnit : , Pixels/Inch
Image YCbCrPositioning : , Centered
Image ExifOffset : , 138
Thumbnail Compression : , JPEG (old-style)
Thumbnail XResolution : , 72
Thumbnail YResolution : , 72
Thumbnail ResolutionUnit : , Pixels/Inch
Thumbnail JPEGInterchangeFormat : , 2042
Thumbnail JPEGInterchangeFormatLength : , 3451
EXIF ExposureTime : , 1/1000000
EXIF FNumber : , 14/5
EXIF ISOSpeedRatings : , 64
EXIF ExifVersion : , 0220
EXIF DateTimeOriginal : , 2012:01:07 09:38:14
EXIF DateTimeDigitized : , 2012:01:07 09:38:14
EXIF ComponentsConfiguration : , YCbCr
EXIF ShutterSpeedValue : , 19931/1000
EXIF ApertureValue : , 297/100
EXIF LightSource : , Unknown
EXIF Flash : , Flash did not fire, compulsory flash mode
EXIF FocalLength : , 37/10
EXIF FlashPixVersion : , 0100
EXIF ColorSpace : , sRGB
EXIF ExifImageWidth : , 1200
EXIF ExifImageLength : , 1600
EXIF CustomRendered : , Normal
EXIF ExposureMode : , Auto Exposure
EXIF WhiteBalance : , Auto
EXIF DigitalZoomRatio : , 1
EXIF SceneCaptureType : , Standard
EXIF GainControl : , Low gain up
"""