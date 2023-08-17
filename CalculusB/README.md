# Michael McCabe's Website


## How it works

The static site is built automatically using GitHub Actions and deployed to https://brian-rose.github.io.
To see how this works, look at `.github/workflows/deploy.yaml` in the source repository.
To mimic this workflow in another repository, note that you need to enable GitHub Pages
for your repo (Setting --> Options --> GitHub Pages).


## How to make changes to the site

Not sure how yet.


## How to build the site locally

You can also built the static site manually by installing sphinx and all dependencies in a python environment. For example, from the source repository:
```
pip install -r requirements.txt
make html
```

You can now view the built site in your web browser with
```
open _build/html/index.html
```
