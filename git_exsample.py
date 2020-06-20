import git
new_repo = git.Repo.init('new_repo')

git.Repo.clone_from("https://github.com/itzikorfa/gitexsample", "gitExample")