import git

git.config("--global", "user.name", "Seu Nome")
git.config("--global", "user.email", "seu_email@email.com")
git.config("--global", "init.defaultBranch", "main")

repo = git.Repo.init(".")
repo.index.add(".")
repo.index.commit("Criando estrutura básica do Django e configurando Git")
