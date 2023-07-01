from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_applicationautoscaling as appscaling,
    aws_ecs_patterns as ecsp,
)
from aws_cdk.aws_ecr_assets import Platform
from constructs import Construct
from pathlib import Path

class InfraStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "Vpc", max_azs=1)
        cluster = ecs.Cluster(self, "EcsCluster", vpc=vpc)
        scheduled_fargate_task = ecsp.ScheduledFargateTask(
            self,
            "ScheduledFargateTask",
            cluster=cluster,
            scheduled_fargate_task_image_options = ecsp.ScheduledFargateTaskImageOptions(
                image=ecs.AssetImage(str(Path('..') / 'app'),
                platform = Platform.LINUX_AMD64),
                memory_limit_mib=512,
            ),
            schedule=appscaling.Schedule.expression("rate(1 day)"),
        )
