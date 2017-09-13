import boto

def get_touchfile(bucket_name, touchfile_name):
	# Connect to S3, get contents of a file
	# based upon bucket name and path to file 
	# within the bucket. Return file's contents.
    s3 = boto.connect_s3()
    bucket = s3.get_bucket(bucket_name, validate=False)
    key = bucket.new_key(touchfile_name)

    contents = key.get_contents_as_string()
    return contents

