class DBBudgetRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """

    route_app_labels = (
        # "aaa",
        # "formula_aaa",
        # "bvs",
        # "formula_bvs",
        # "vcs",
        # "formula_vcs",
        # "budgetapp",
        # "budget_vcst",
        "budgetapp"
    )

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label == "vcs_kanban":
            return "kanban_vcst"

        return "default"

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label == "vcs_kanban":
            return "kanban_vcst"

        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        print("Allow relations if a model in the auth or contenttypes apps")
        # if (
        #     obj1._meta.app_label in self.route_app_labels
        #     or obj2._meta.app_label in self.route_app_labels
        # ):
        #     return True

        # if (
        #     obj1._meta.app_label == "budgetapp"
        #     or obj2._meta.app_label == "budgetapp"
        # ):
        #     return True

        # return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label == "vcs_kanban":
            return None

        return True
