from django.urls import path
from .views import *


urlpatterns = [
	path('', PostListView.as_view(), name='post-list'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
	path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
	path('post/<int:post_pk>/comment/delete<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
	path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
	path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
	path('profile/<int:pk>/followers/add/', AddFollowers.as_view(), name='add-follower'),
	path('profile/<int:pk>/followers/remove/', RemoveFollowers.as_view(), name='remove-follower'),
	path('post/<int:pk>/like/', AddLike.as_view(), name='like'),
	path('post/<int:post_pk>/comment/<int:pk>/like/', AddCommentLike.as_view(), name='comment-like'),
	path('post/<int:pk>/dislike/', DisLike.as_view(), name='dislike'),
	path('post/<int:post_pk>/comment/<int:pk>/dislike/', CommentDisLike.as_view(), name='comment-dislike'),
	path('search/', UserSearch.as_view(), name='profile-search'),
	path('profile/<int:pk>/followers/', ListFollowers.as_view(), name='list-followers'),
	path('post/<int:post_pk>/comment/<int:pk>/reply', CommentReply.as_view(), name='comment-reply'),
	path('notification/<int:notification_pk>/post/<int:post_pk>/', PostNotification.as_view(), name='post-notification' ),
	path('notification/<int:notification_pk>/profile/<int:profile_pk>/', FollowNotification.as_view(), name='follow-notification' ),
	path('notification/delete/<int:notification_pk>/', RemoveNotification.as_view(), name='notification-delete'),
	path('inbox/', ListThreads.as_view(), name='inbox'),
	path('inbox/create-thread/', CreateThread.as_view(), name='create-thread'),
	path('inbox/<int:pk>/', ThreadView.as_view(), name='thread'),
	path('inbox/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message'),
	path('notification/<int:notification_pk>/thread/<object_pk>/', ThreadNotification.as_view(), name='thread-notification'),
	path('post/<int:pk>/share/', SharePostView.as_view(), name='share-post'),
	path('explore/', Explore.as_view(), name='explore'),
]