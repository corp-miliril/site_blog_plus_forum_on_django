from .models import Discussion, AdvUser, ForumLikes
from collections import Counter 

def forum_context_processor(request):
	context = {}

	if Discussion.objects.all():

		max_ = max([dis.forumlikes_set.all().count() for dis in Discussion.objects.all()])
		for dis in Discussion.objects.all():
			if dis.forumlikes_set.all().count() == max_:
				context['popular_discuss'] = dis


	context['user_rating'] = sum([dis.forumlikes_set.all().count() for dis in Discussion.objects.filter(creator=request.user.pk)])

	if AdvUser.objects.count() >= 3:
		top = {}
		for cur_user in AdvUser.objects.all():
			top[cur_user] = sum([dis.forumlikes_set.all().count() for dis in Discussion.objects.filter(creator=cur_user.pk)])


		k = Counter(top)
		high = k.most_common(3) 

		
		context['first_place'] = high[0][0]
		context['first_place_rating'] = high[0][1]

		context['second_place'] =high[1][0]
		context['second_place_rating'] = high[1][1]

		context['third_place'] = high[2][0]
		context['third_place_rating'] = high[2][1]

	return context