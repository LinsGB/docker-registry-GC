import os
import shutil
import glob

def garbageCollect ():
	repoDir = '/Users/atngabriel/docker-registry/data/docker/registry/v2/repositories'
	repos = os.listdir(repoDir)
	for repo in repos:
		tagsDir = repoDir+'/'+repo+'/_manifests/tags/'
		revisionsSha256Dir = repoDir+'/'+repo+'/_manifests/revisions/sha256/'
		tags = glob.glob(tagsDir+'*')
		revisionsSha256 = glob.glob(revisionsSha256Dir+'*')
		currentTag = max(tags, key=os.path.getctime)
		tags.remove(currentTag)
		for tag in tags:
			shutil.rmtree(tag)
		sha256 = glob.glob(currentTag+'/index/sha256/*')[0].replace(currentTag+'/index/sha256/','')
		revisionsSha256.remove(repoDir+'/'+repo+'/_manifests/revisions/sha256/'+sha256)
		for revisionSha256 in revisionsSha256:
			shutil.rmtree(revisionSha256)
	os.system('/bin/registry garbage-collect ~/docker-registry/config.yml')
garbageCollect()
