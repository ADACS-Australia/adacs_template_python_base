(configing-new)=
# Configuring a New Project

Develpers and project owners/maintainers will require accounts with one or all of the following services to work with this codebase.  This section details how these services need to be configured.  Following these steps should only be necessarry - or partially necessary - if a developer chooses to fork the project.

1. [***GitHub***](https:/github.com)

    To work with this codebase, you will require a *GitHub* account ([go here to get one](https://github.com)).
    
    Branch permissions for the main project repository should be configured only permit merges from pull requests.  To do so, navigate to `Settings->Branches->Add branch ruleset` and:

    - give the Ruleset whatever name you'd like (e.g. `Protect Main`)
    - set `Enforecement status` to `Active`
    - add a `Target Branch` targeting criteria by pattern and type `main`
    - select `Require a pull request before merging`
    - select `Require status checks to pass` and add `Run all build and unit tests` from GitHub Actions as a required check

    This will ensure that all CI/CD tests pass before a merge to the main branch can be made.
    
    Several secrets need to be configured by navigating to `Settings->Secrets->Actions` and adding the following:
    
    - To host the project documentation on *Read the Docs* (see below), the following secrets need to be set (see below for where to find these values):
    
        - **RTD_WEBHOOK_TOKEN**, and
        - **RTD_WEBHOOK_URL**
    
    - To make code releases available on the **Python Package Index** (see below), then the following secret needs to be set (see below for where to find this value):
    
        - **PYPI_TOKEN**,
    
    - To test code releases with the **Test Python Package Index** (see below), then the following secret needs to be set (see below for where to find this value):
    
        - **TEST_PYPI_TOKEN**,


2. [__Read the Docs__](https://readthedocs.org)

    **Read the Docs** (*RTD*) is used to build and host the project documentation.  An account is needed if you are an owner/maintainer of the project and will be publishing and managing the project's documentation online, but not needed if you are simply a contributing developer.  *RTD* can be configured in either of the following ways:

    1. **By connecting *RTD* to your *GitHub* account**
        - Ensure that your *GitHub* account has been connected.  This is done automatically if you log into *RTD* with your *GitHub* credentials.  If you logged in with your email, navigate to `<login_id>->Settings->Connected Services` by clicking on "Connect Your Accounts" and click "Connect to GitHub".  You know your account is linked if it is listed below under "Active Services".

        - Return to your *RTD* landing page by clicking on your account name at the top.  Click "Import a Project".  Your *GitHub* repository should be listed here (you may need to refresh the list if it has been created recently).  Import it.

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

    This service is used to publish project releases.  An account is needed if you are the owner of the project, but not generally needed if you are simply a contributing developer.  An API token will need to be created and added to your *GitHub* project as **PYPI_TOKEN** (as detailed above).  This can be generated from the *PyPI* UI by navigating to `Account Settings->Add API Token`.

    To test releases, a parallel account on *test.PyPI* is needed and a similar token to **PYPI_TOKEN** - named **TEST_PYPI_TOKEN** needs to be set, in the same way as above.  To create a test release, flag it as a "pre-release" through the *GitHub* interface when you generate a release, and it will be published on *test.PyPI.org* rather than *PyPI.org*.  If this token is not defined, publication will not happen on either.

    ::: {note}
    Although `poetry` can be used to directly publish this project to *PyPI*, users should not do this.  The proper way to publish the project is through the *GitHub* interface, which leverages the *GitHub Workflows* of this project to ensure the enforcement of project standards before a new version can be created.
    :::
