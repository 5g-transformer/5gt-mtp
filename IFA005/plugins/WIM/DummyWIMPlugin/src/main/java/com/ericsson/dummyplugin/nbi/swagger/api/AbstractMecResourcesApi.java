package com.ericsson.dummyplugin.nbi.swagger.api;

import com.ericsson.dummyplugin.nbi.swagger.model.InlineResponse200;

import javax.ws.rs.*;
import javax.ws.rs.core.Response;

import io.swagger.annotations.*;

import java.util.Map;
import java.util.List;
import javax.validation.constraints.*;
import javax.validation.Valid;

@Path("/abstract-mec-resources")
@Api(description = "the abstract-mec-resources API")
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaJAXRSSpecServerCodegen", date = "2019-05-22T09:15:25.142Z")
public class AbstractMecResourcesApi {

    @GET
    @Produces({ "application/json" })
    @ApiOperation(value = "Retrieve MEC specific info for MEC PoP capable", notes = "Retrieve MEC specific info for MEC PoP capable", response = InlineResponse200.class, tags={ "MECResources" })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "Successful operation", response = InlineResponse200.class),
        @ApiResponse(code = 400, message = "Bad request", response = Void.class),
        @ApiResponse(code = 401, message = "Unauthorized", response = Void.class),
        @ApiResponse(code = 403, message = "Forbidden", response = Void.class)
    })
    public Response collectMecAbstractedInformation() {
        return Response.ok().entity("magic!").build();
    }
}
