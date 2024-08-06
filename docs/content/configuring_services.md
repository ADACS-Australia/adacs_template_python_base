(configing-new)=
# Configuring a New Project

Develpers and project owners/maintainers will require accounts with one or all of the following services to work with this codebase.  This section details how these services need to be configured.  Following these steps should only be necessarry - or partially necessary - if a developer chooses to fork the project.

1. [***GitHub***](https:/github.com)

    To work with this codebase, you will require a *GitHub* account ([go here to get one](https://github.com)).
    
    ::: {note}
    If you have just rendered a new project and have followed the instructions that were given, you should already have done the
    following.  For completeness though - or in case you are looking to configure a fork of a project - we note that the following
    needs to be done:
    :::

    Branch permissions for the main project repository should be configured to only permit merges from pull requests.  To do so, navigate to `Settings->Branches->Add branch ruleset` and:

    - give the Ruleset whatever name you'd like (e.g. `Protect Main`)
    - set `Enforecement status` to `Active`
    - add a `Target Branch` targeting criteria by pattern and type `main`
    - select `Require a pull request before merging`
    - select `Require status checks to pass` and add `Run all build and unit tests` from GitHub Actions as a required check

    This will ensure that all CI/CD tests pass before a merge to the main branch can be made.
    
    ::: {note}
    For those who have just rendered a new project, followed the instructions and are continuing to configure it, you need to do
    the following:
    :::

    Several (optional) secrets need to be configured by navigating to `Settings->Secrets->Actions` and adding the following:
    
    - To host the project documentation on *Read the Docs* (see below), the following secrets need to be set (see below for where to find these values):
    
        - **RTD_WEBHOOK_TOKEN**, and
        - **RTD_WEBHOOK_URL**
    
    - To make code releases available on the **Python Package Index** (see below), then the following secret needs to be set (see below for where to find this value):
    
        - **PYPI_TOKEN**,
    
    - To test code releases with the **Test Python Package Index** (see below), then the following secret needs to be set (see below for where to find this value):
    
        - **TEST_PYPI_TOKEN**,


2. [__Read the Docs__](https://readthedocs.org)

    ::: {note}
    **Read the Docs** (*RTD*) is used to build and host the project documentation.  To take advantage of this functionality, this service needs to be configured by the owner/maintainer of the project.  Contributing developers or those who don't wish to have documentation published on *RTD* can ignore the following.
    :::

    To (optionally) publish this project's documentation you will need a *RTD* account ([go here to get one](https://readthedocs.org)).  It can be configured in either of the following ways:

    1. **By connecting *RTD* to your *GitHub* account**
        - Ensure that your *GitHub* account has been connected.  This is done automatically if you log into *RTD* with your *GitHub* credentials.  If you logged in with your email, navigate to `<login_id>->Settings->Connected Services` by clicking on `Connect Your Accounts` and click `Connect to GitHub`.  You know your account is linked if it is listed below under `Active Services`.

        - Return to your *RTD* landing page by clicking on your account name at the top.  Click `Import a Project`.  Your *GitHub* repository should be listed here (you may need to refresh the list if it has been created recently).  Import it.

        - To obtain **RTD_WEBHOOK_TOKEN**, navigate to `<Account>->Settings->API Tokens` on *Read the Docs*.  If a token has been created already, you can use it.  Otherwise (or if you want a token specifically for this project), create a new one.

        - To obtain **RTD_WEBHOOK_URL**, migrate to the `Admin->Integrations` tab on the *RTD* project page.  Click on your incomming webhook and get the URL there.

    2. **By creating a Generic Webhook**
        - Navigate to the `Admin->Integrations` tab on the *RTD* project page and click `Add integration`.  Then select `Generic API incoming webhook` from the dropdown and click `Add integration`.

        - To obtain **RTD_WEBHOOK_URL** and **RTD_WEBHOOK_TOKEN**, migrate to the `Admin->Integrations` tab on the *RTD* project page and click on your incomming webhook.

    Once properly configured, the documentation for this project should build automatically on *RTD* every time you [generate a new release](#new-release).

    ::: {note}
    Make sure **RTD_WEBHOOK_URL** starts with `https://`.  Prepend it if not.
    :::

(config-pypi)=
3. The [__Python Package Index (*PyPI*)__](https://pypi.org)

    ::: {note}
    **The Python Package Index** (*PyPI*) and **The Test Python Package Index (*TestPyPI*) are used to publish code releases.  To take advantage of this functionality, this service needs to be configured by the owner/maintainer of the project.  Contributing developers or those who don't wish to have documentation published on *RTD* can ignore the following.
    :::

    To (optionally) publish releases of this project's code you will need a *PyPI* account ([go here to get one](https://pypi.org)).  To (optionally) generate test releases, you will need a *TestPyPI* account.  They operate the same way and can both be configured as follows:

        - An API token will need to be created and added to your *GitHub* project as **PYPI_TOKEN** (as detailed above).  This can be generated from the *PyPI* UI by navigating to `Account Settings->Add API Token`.  In the first instance - before the project exists on your account - generate a token with `Entire Account` scope.  Once the project has been published for a first time to *PyPI*, the initial token can be deleted and a new one generated with an project scope selected to be that of the project.  Make sure to update the *GitHub* secret value once you have done so.

        - Repeat this process for *TestPyPI* if you want to be able to generate test releases, adding it as a secret to your *GitHub* repo with the name **TEST_PYPI_TOKEN**

    ::: {note}
    To create a test release, flag it as a `pre-release` through the *GitHub* interface when you generate a release, and it will be published on *test.PyPI.org* rather than *PyPI.org*.  If this token is not defined, publication will not happen on either, if this option is flagged.
    :::

    ::: {note}
    Although `poetry` can be used to directly publish this project to *PyPI*, users should not do this.  The proper way to publish the project is through the *GitHub* interface, which leverages the *GitHub Workflows* of this project to ensure the enforcement of project standards before a new version can be created.
    :::
