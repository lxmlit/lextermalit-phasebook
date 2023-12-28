from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    ## NOTE: I have included a "BizKit Interview Task Test Samples.pdf" file for my testing.

    # empty list
    search_result = []

    # iterate through the USERS. Based on search specification
    for user in USERS:
        # setting order for Bonus Challenge.
        # this will make sure that the results are sorted based on this order:
        # id, name, age, occupation
        order = 0
        if 'id' in args and user['id'] == args['id']:
            order += 4
                
        if 'name' in args and args['name'].lower() in user['name'].lower():
            order += 3
                
        if 'age' in args and int(args['age']) - 1 <= user['age'] <= int(args['age']) + 1:
            order += 2

        if 'occupation' in args and args['occupation'].lower() in user['occupation'].lower():
            order += 1

        # append the result. this also works if there are no search parameter is enterede
        if order > 0 or not args:
            user['order'] = order
            search_result.append(user)

    # sorts search_result in reverse
    search_result.sort(key=lambda x: x['order'], reverse=True)

    # delete "order" from search_result
    for user in search_result:
        del user['order']
         
    #return the result
    return search_result
