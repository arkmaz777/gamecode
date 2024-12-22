from django.contrib.auth.decorators import login_required

import json
import random
from django.shortcuts import render
from . models import Result

@login_required(login_url='/')
def play(request):
    if request.method == 'POST':
        reel_values = ['J', 'Q', 'K', 'A']
        reels_combination = []
        for _ in range(3):
            reels_combination.append(random.choice(reel_values))

        reels_combination_json = json.dumps(reels_combination)
        game_result = result_evaluation(reels_combination)

        user = request.user
        result = Result(
            id_auth_user=user,
            reels_combination=reels_combination,
            game_result=game_result
        )
        result.save()

        current_user_last_10_results = Result.objects.filter(id_auth_user=user).order_by('-id')[:10]
        # last_10_results = Result.objects.order_by('-id')[:10]
        last_10_results = Result.objects.select_related('id_auth_user').order_by('-id')[:10]


        return render(request,
                      'play.html',
                      {
                          'reels_combination': reels_combination,
                          'game_result': game_result,
                          'current_user_last_10_results': current_user_last_10_results,
                          'last_10_results': last_10_results,
                      }
                  )

    return render(request,'play.html')


def result_evaluation(reels_combination):
    """
    Evaluate the result of a slot game based on a combination of symbols
    which comes from a deck o playing cards.

    Corresponding score based on the symbol:
    - 'J' -> 1
    - 'Q' -> 2
    - 'K' -> 3
    - 'A' -> 4
    If the symbols are not the same, it returns 0.

    Parameters:
    reels_combination (list): A list containing exactly three symbols, where each symbol is a string
                               representing a reel outcome (one of 'J', 'Q', 'K', or 'A').

    Returns:
    int: A score based on the symbol if all symbols in `reels_combination` are the same.
         Returns 0 if the symbols are not the same.

    Raises:
    ValueError: If the length of `reels_combination` is not equal to 3.
    """
    if len(reels_combination) != 3:
        raise ValueError('Incorrect length of the list `reels_combination`!')

    result_values = {'J': 1, 'Q': 2, 'K': 3, 'A': 4}
    all_same = all(x == reels_combination[0] for x in reels_combination)
    if not all_same:
        return 0

    return result_values[reels_combination[0]]

