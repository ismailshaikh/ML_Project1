## ML_Project1

### Software and Account Requirements:

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS-Code IDE](https://code.visualstudio.com/download)
4. [Git-cli](https://git-scm.com/downloads).
5. [Git-Command-Documentation](https://git-scm.com/docs/git)


# Creating conda environment

'''
conda create -p venv python==3.7 -y
'''

'''
conda activate venv/
'''

or

'''
conda activate venv
'''

'''
pip install -r requirements.txt
'''

'''
To Add Files to git
'''

'''
git add
'''

or

'''
git add < file name >
'''

> Note :To Ignore file or folder from git we can write name of file/folder in.gitignore file

#### To Check the git status

'''
git status
'''

#### To check all version maintained by git

'''
git log
'''

#### To create version/commit all changes by git:

'''
git commit-m "message"
'''

#### To Send version/changes to github

'''
git push origin main
'''

#### To Check remote url

'''
git remote -v
'''

#### To setup CI/CD pipeline in heroku we need 3 information

1. Heroku_Email = 'ismail46h.shaikh@gmail.com'.
2. Heroku_API_Key = <>.
3. Heroku_App_Name = machine-learning-practice.


#### BUILD DOCKER IMAGE

'''
docker build -t <image_name>:<tagname> .
'''

> Note: Image name for docker must be lowercase


#### To list docker image

'''
docker images
'''

#### Run Docker image

'''
docker run -p 5000:5000 -e PORT= 5000
'''

#### To Check Running container in docker

'''
docker ps
'''

#### To stop docker container

'''
docker stop <container_id>
'''


'''
python setup.py install
'''