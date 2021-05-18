# lambda-with-pytorch-container

This is a blank project for TypeScript development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

## Useful commands

 * `npm run build`   compile typescript to js
 * `npm run watch`   watch for changes and compile
 * `npm run test`    perform the jest unit tests
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk synth`       emits the synthesized CloudFormation template

## 説明
api gateway - lambda w/containerで構成されている。

画像とその他のデータを含むmultipart/form-dataのリクエストから
画像だけ取り出しResNet50で適当に処理して適当に値を返す。

## develop api
### develop in local
```bash
# in /api/lambda
poetry install
```

### run local
```bash
# in /api/lambda
docker-compose up --build

curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```
jsonしかうまく送れないかも

## deploy api
```bash
# in /api
npx cdk deploy --profile ${aws_profile_name}
```
