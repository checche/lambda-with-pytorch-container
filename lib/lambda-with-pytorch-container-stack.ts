import * as cdk from '@aws-cdk/core';
import * as apigw from '@aws-cdk/aws-apigateway';
import * as lambda from '@aws-cdk/aws-lambda';

export class LambdaWithPytorchContainerStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const projectName = this.node.tryGetContext('projectName')

    const hello = new lambda.DockerImageFunction(this, `${projectName}Handler`, {
      code: lambda.DockerImageCode.fromImageAsset('lambda'),
      timeout: cdk.Duration.minutes(1),
      memorySize: 2048
    });

    const api = new apigw.LambdaRestApi(this, `${projectName}Endpoint`, {
      handler: hello,
      binaryMediaTypes: ['*/*'],
    });
  }
}
