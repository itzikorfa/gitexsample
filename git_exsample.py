import git
# repo = git.Repo.init('gitExample2')
try:
    git.Repo.clone_from("https://github.com/itzikorfa/gitexsample", "gitExample3")
except Exception as e:
    repo = git.Repo.init('gitExample3')
    print(e)
    repo.remote().pull()
#
#
# if repo.is_dirty():
#     print("changes exists")
# repo.remote().pull()
# # git.Repo.clone_from("https://github.com/itzikorfa/gitexsample", "gitExample")