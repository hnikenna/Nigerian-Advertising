import random, string
from django.http import HttpResponseRedirect


def breadcrumb(text: str, num: int):
    if len(text) > num:
        return text[:num].rstrip(' ') + '...'
    else:
        return text.rstrip(',').rstrip('.')


def go_back(request):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def display(var):
    # exec(print('Var:', var))
    command = f'{var=}'.split('=')[0].title() + f': {var}'
    print(command)


def randx(len):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=len))


def anon_id(self, starter="ax", amount=12):
    error_count = 0
    starter += '-'
    while not self.anon_id:
        error_count += 1
        key = starter + randx(amount)
        self.anon_id = key
        # Start test for coincidental repeated id
        # self.anon_id = 'rc-ggvzzpxjpfgd' # already assigned key
        try:
            self.save()
        except:
            self.anon_id = ''
        if error_count == 5:
            break

    # print('ID:', self.anon_id)
    return self.anon_id


def format_currency(value):
    return "{:,.2f}".format(value)


def duplicate_count(all_texts:list, new_texts: list):
    count = 0
    for text in new_texts:
        if text in all_texts:
            count += 1
        for option in all_texts:        # will return 'creflist' if you search 'cref'
            if text in option:
                count += 1
    return count

