from django.shortcuts import get_object_or_404, reverse, redirect


# def toggle_activity(request, View, pk):
#     view_item = get_object_or_404(View, pk=pk)
#     if view_item.is_active:
#         view_item.is_active = False
#     else:
#         view_item.is_active = True
#     view_item.save()
#     return redirect(reverse('catalog:blog_records'))
