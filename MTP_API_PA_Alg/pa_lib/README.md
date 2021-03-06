# swagger-java-client

5GT-MTP PA API
- API version: 0.0.0
  - Build date: 2019-05-02T08:45:54.546Z

REST-API for the MTP PA. Find more at http://5g-transformer.eu


*Automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen)*


## Requirements

Building the API client library requires:
1. Java 1.7+
2. Maven/Gradle

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>io.swagger</groupId>
  <artifactId>swagger-java-client</artifactId>
  <version>1.0.0</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
compile "io.swagger:swagger-java-client:1.0.0"
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/swagger-java-client-1.0.0.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.InterNfviPopCompRouteApi;

import java.io.File;
import java.util.*;

public class InterNfviPopCompRouteApiExample {

    public static void main(String[] args) {
        
        InterNfviPopCompRouteApi apiInstance = new InterNfviPopCompRouteApi();
        String interNfviConnectivityId = "interNfviConnectivityId_example"; // String | Identifier of the interNfviPop connection to be computed.
        CompRouteInput params = new CompRouteInput(); // CompRouteInput | 
        try {
            InlineResponse200 result = apiInstance.compRouteInterNfviPop(interNfviConnectivityId, params);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InterNfviPopCompRouteApi#compRouteInterNfviPop");
            e.printStackTrace();
        }
    }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*InterNfviPopCompRouteApi* | [**compRouteInterNfviPop**](docs/InterNfviPopCompRouteApi.md#compRouteInterNfviPop) | **POST** /compRoute/{interNfviConnectivityId} | Computes the interNfviPop connectivity between a pair of PEs with specific network constraints and selects specific servers/hosts within NfviPops


## Documentation for Models

 - [CompRouteInput](docs/CompRouteInput.md)
 - [CompRouteInputAbsWanTopo](docs/CompRouteInputAbsWanTopo.md)
 - [CompRouteInputComputeReqs](docs/CompRouteInputComputeReqs.md)
 - [CompRouteInputCpuResourceAttributes](docs/CompRouteInputCpuResourceAttributes.md)
 - [CompRouteInputEdges](docs/CompRouteInputEdges.md)
 - [CompRouteInputInterWanLinks](docs/CompRouteInputInterWanLinks.md)
 - [CompRouteInputMemoryResourceAttributes](docs/CompRouteInputMemoryResourceAttributes.md)
 - [CompRouteInputNetwLinkQoS](docs/CompRouteInputNetwLinkQoS.md)
 - [CompRouteInputNfviPopReqs](docs/CompRouteInputNfviPopReqs.md)
 - [CompRouteInputNfviPops](docs/CompRouteInputNfviPops.md)
 - [CompRouteInputNodes](docs/CompRouteInputNodes.md)
 - [CompRouteInputQosCons](docs/CompRouteInputQosCons.md)
 - [CompRouteInputResourceZoneAttributes](docs/CompRouteInputResourceZoneAttributes.md)
 - [CompRouteInputStorageResourceAttributes](docs/CompRouteInputStorageResourceAttributes.md)
 - [CompRouteOutput](docs/CompRouteOutput.md)
 - [CompRouteOutputInterWanLinks](docs/CompRouteOutputInterWanLinks.md)
 - [CompRouteOutputNfviPopResp](docs/CompRouteOutputNfviPopResp.md)
 - [CompRouteOutputWanPathElements](docs/CompRouteOutputWanPathElements.md)
 - [CompRouteOutputWanPaths](docs/CompRouteOutputWanPaths.md)
 - [CompRouteOutputZoneAtts](docs/CompRouteOutputZoneAtts.md)
 - [InlineResponse200](docs/InlineResponse200.md)


## Documentation for Authorization

All endpoints do not require authorization.
Authentication schemes defined for the API:

## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

cnd@lists.cttc.es

