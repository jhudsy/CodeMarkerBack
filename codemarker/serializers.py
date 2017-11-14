from rest_framework import serializers

from codemarker.models import Course, Assessment, Submission


class SubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submission
        fields = '__all__'
        extra_kwargs = {
            'url': {
                'view_name': 'submission:submissions-detail',
            }
        }

class AssessmentSerializer(serializers.ModelSerializer):

    submissions = SubmissionSerializer(many=True, read_only=True)

    class Meta:
        model = Assessment
        fields = '__all__'
        extra_kwargs = {
            'url': {
                'view_name': 'assessment:assessments-detail',
            }
        }


class CourseSerializer(serializers.ModelSerializer):

    assessments = AssessmentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'created_at', 'updated_at', 'assessments')
        extra_kwargs = {
            'url': {
                'view_name': 'course:courses-detail',
            }
        }



