from rest_framework import serializers
from poll.models import TaskImage, Task


class TaskImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskImage
        fields = ('image',)

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    images = TaskImageSerializer(source='taskimage_set', many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'images')

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        task = Task.objects.create(title=validated_data.get('title', 'no-title'))
        for image_data in images_data.values():
            TaskImage.objects.create(task=task, image=image_data)
        return task
#
# class ChoiceSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(required=False)
#
#     class Meta:
#         model = Choice
#         fields = [
#             'id',
#             'question',
#             'text'
#         ]
#         read_only_fields = ('question',)
#
# class QuestionSerializer(serializers.ModelSerializer):
#     choices = ChoiceSerializer(many=True)
#
#     class Meta:
#         model = Question
#         fields = [
#             "id",
#             "title",
#             "status",
#             "created_by",
#             "choices",
#         ]
#
#     def create(self, validated_data):
#         choices = validated_data.pop('choices')
#         question = Question.objects.create(**validated_data)
#         for choice in choices:
#             Choice.objects.create(**choice, question=question)
#         return question
# from rest_framework import serializers
# from exam.models import Post, Image
#
#
# class ImageSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Image
#         fields = '__all__'
#
#
# class PostSerializer(serializers.ModelSerializer):
#     images = ImageSerializer(many=True)
#
#     class Meta:
#         model = Post
#         fields = '__all__'
#
#     def create(self, validated_data):
#         """
#         Handle writable nested serializer to create a new post.
#         :param validated_data: validated data, by serializer class's validate method
#         :return: updated Post model instance
#         """
#         # TODO: Handle the case to avoid new Post instance creation if Image model data have any errors
#         data = validated_data.copy()
#         data.pop('images')  # deleting 'images' list as it is not going to be used
#
#         '''
#         Fetching `images` list of image files explicitly from context.
#         Because using default way, value of `images` received at serializers from viewset was an empty list.
#         However value of `images` in viewset were OK.
#         Hence applied this workaround.
#         '''
#         images_data = self.context.get('request').data.pop('images')
#         try:
#             post = Post.objects.create(**data)
#         except TypeError:
#             msg = (
#                     'Got a `TypeError` when calling `Post.objects.create()`.'
#             )
#             raise TypeError(msg)
#         try:
#             for image_data in images_data:
#                 # Image.objects.create(post=post, **image_data)
#                 image, created = Image.objects.get_or_create(image=image_data)
#                 post.images.add(image)
#
#             return post
#         except TypeError:
#             post = Post.objects.get(pk=post.id)
#             post.delete()
#             msg = (
#                     'Got a `TypeError` when calling `Image.objects.get_or_create()`.'
#             )
#             raise TypeError(msg)
#
#         return post
#
#     def update(self, instance, validated_data):
#         """
#         Handle writable nested serializer to update the current post.
#         :param instance: current Post model instance
#         :param validated_data: validated data, by serializer class's validate method
#         :return: updated Post model instance
#         """
#         # TODO: change the definition to make it work same as create()
#
#         '''
#         overwrite post instance fields with new data if not None, else assign the old value
#         '''
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.thumbnail = validated_data.get('thumbnail', instance.thumbnail)
#         # instance.updated_at = validated_data.get('updated_at', instance.updated_at)  # no need to update; auto_now;
#
#         try:
#
#             '''
#             Fetching `images` list of image files explicitly from context.
#             Because using default way, value of `images` received at serializers from viewset was an empty list.
#             However value of `images` in viewset were OK.
#             Hence applied this workaround.
#             '''
#             images_data = self.context.get('request').data.pop('images')
#         except:
#             images_data = None
#
#         if images_data is not None:
#             image_instance_list = []
#             for image_data in images_data:
#                 image, created = Image.objects.get_or_create(image=image_data)
#                 image_instance_list.append(image)
#
#             instance.images.set(image_instance_list)
#
#         instance.save()  # why? see base class code; need to save() to make auto_now work
#         return instance
