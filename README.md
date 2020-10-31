# Day Eight :: Filtering/...


## Difference Between Default Router and Simple Router.
- Default Router allows you to specify the format of response like.
  - `http://localhost:8000/teachers.json`
  - `http://localhost:8000/teachers.api`
- or
  - `http://localhost:8000/teachers?format=json`
  - `http://localhost:8000/teachers?format=api`

- But when we use `SimpleRouter` class then only later is allowed.
  - `http://localhost:8000/teachers?format=json`
  - `http://localhost:8000/teachers?format=api`



## Format Suffix Pattern:
- Location: `from rest_framework.urlpatterns import format_suffix_patterns`
- Used to modify url patterns.
> The error will be caused if you try to use `DefaultRouter` with `format_suffix_patterns`.
### Why we use `format_suffix_patterns`
- It's use to modify the url patterns so that we can provide the `.jon/api` kind of format.

## How to work with Images in rest framework.
### Set the `MEDIA_URL` and `MEDIA_ROOT`.
- Open `settings.py` and add the following:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'
```
### Handling Url's for Media Files:
- Import the following lines in `urls.py`
```python
from django.conf import settings
from django.conf.urls.static import static
```
- Add this line after your `urlpatterns`
```python
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- Now take a look at the below view.
```python
class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]
    parser_classes = [MultiPartParser]
```


## Filtering
- The basic way to filter is by overwriting the `get_queryset` method of Generic Views.
> Note that Viewsets also have the generic view.
- Take a look at this example:
```python
class PurchaseList(generics.ListAPIView):
    serializer_class = PurchaseSerializer

    def get_queryset(self):
        """
        Request obj.: self.request
        How to get that parameters of get request.        
        1. username = self.kwargs['username']
        2. username = self.request.query_params.get('username', None)
        """
        username = self.request.query_params.get('username', None)
        return Purchase.objects.filter(purchaser__username=username)

```

## Search Filter Class
- Location: `form rest_framework.filters import SearchFilter`
```python
from rest_framework import filters

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']
```
- When you make queries like: `http://example.com/api/users?search=russell`
- Then our view will try to `username` and `email` match with `russell`. 
- If you use ['=username'] then it'll try to match exact result.
- If you use ['^username'] then it'll try to match the results which starts with the given query.