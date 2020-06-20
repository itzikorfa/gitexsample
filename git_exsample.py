import git
new_repo = git.Repo.init('new_repo')
# this is an update
git.Repo.clone_from("https://github.com/itzikorfa/gitexsample", "gitExample")
