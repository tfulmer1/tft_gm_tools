from django.shortcuts import render
from apps import compute_raw_probabilities, compute_value_or_below
from django.http import HttpResponse


# Create your views here.
def index(request):
    dice, sides = 5,6
    probs = compute_raw_probabilities(dice,sides)
    response = []
    start = '''
            <table>
              <tr>
                <th>Value</th>
                <th>Probability</th>
                <th>Graph</th>
              </tr>
            '''
    response.append(start)
    for x in range(dice,(dice*sides)+1):
        prob = 100*compute_value_or_below(probs,x)
        stars = "|" + "|"*int(prob)
        response.append("""  <tr>
                               <td>{0} or less</td>
                               <td>{1:.2f}</td>
                               <td>{2}</td>
                              </tr>""".format(x, prob, stars))
        response.append('</table>')
    return HttpResponse("<br>".join(response))
