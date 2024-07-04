# from rest_framework_simplejwt.tokens import AccessToken
# from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
# from django.utils.deprecation import MiddlewareMixin
# from account.models import User
# from rest_framework.response import Response
# from rest_framework.exceptions import AuthenticationFailed
# import jwt
# from jwt.exceptions import ExpiredSignatureError

# class TokenValidationMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         auth = request.headers.get('Authorization', None)
#         if auth and auth.startswith('Bearer '):
#             token_str = auth.split(' ')[1]
#             try:
#                 # Decode the token to retrieve user_id and iat
#                 token = AccessToken(token_str)
                
                
#                 # Retrieve user from database
#                 user = User.objects.get(id=token['user_id'])
#                 latest_token = user.latest_token
#                 decoded_latest_token = jwt.decode(latest_token, options={"verify_signature": False})
#                 # Compare encoded fields with latest_token
#                 if token['user_id'] != user.id or token['iat'] != decoded_latest_token.get('iat'):
#                     raise AuthenticationFailed("Invalid token.")
                
#             except ExpiredSignatureError:
#                 raise AuthenticationFailed("Token has expired.")
#             except (User.DoesNotExist, InvalidToken, TokenError):
#                 raise AuthenticationFailed("Invalid token.")

#         return None