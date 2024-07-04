# from rest_framework_simplejwt.tokens import RefreshToken

# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)
    
#     # Store the latest refresh token in the user model
#     user.latest_token = str(refresh)  # Store access token instead of refresh token
#     user.save()
    
#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }
