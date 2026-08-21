from assertpy import assert_that, soft_assertions


def get_users():
    return [
        {'id': 1, 'name': 'Den', 'age': 20, 'job': [{'id': 1, 'title': 'QA'}]},
        {'id': 2, 'name': 'Alex', 'age': 30},
        {'id': 3, 'name': 'Igor', 'age': 40, 'job': None},
        {'id': 4, 'name': 'Ivan', 'age': 50, 'job': [{'id': 2, 'title': 'CEO'}]},
        {'id': 5, 'name': 'Mon', 'age': 60, 'job': [{'id': 1, 'title': 'QA'}]},
        {'id': 6, 'name': 'Viktor', 'age': 70, 'job': [{'id': 3, 'title': 'Retired'}]},
        {'id': 7, 'name': 'Maria', 'age': 20, 'job': [{'id': 1, 'title': 'DevOps'}]},
        {'id': 8, 'name': 'Anna', 'age': 20, 'job': []},
        {'id': 9, 'name': 'Olha', 'job': [{'id': 1, 'title': 'DevOps'}]},
    ]


class TestUsers:

    def test_users_have_job(self):
        """
        Each user must have a job and it must not be empty.
        """
        users = get_users()

        with soft_assertions():
            for user in users:
                job = user.get("job")

                assert_that(
                    job,
                    description=f"User {user['name']} job"
                ).is_not_none()

                if job is not None:
                    assert_that(
                        job,
                        description=f"User {user['name']} job"
                    ).is_not_empty()
