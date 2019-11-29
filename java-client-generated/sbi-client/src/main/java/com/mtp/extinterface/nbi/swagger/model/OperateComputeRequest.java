/*
 * MTP Manager API
 * MTP Manager API
 *
 * OpenAPI spec version: 2.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package com.mtp.extinterface.nbi.swagger.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * Message for request the operating change of the compute resources
 */
@ApiModel(description = "Message for request the operating change of the compute resources")
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2019-08-05T11:05:49.089Z")
public class OperateComputeRequest {
  @SerializedName("computeId")
  private String computeId = null;

  @SerializedName("computeOperation")
  private String computeOperation = null;

  public OperateComputeRequest computeId(String computeId) {
    this.computeId = computeId;
    return this;
  }

   /**
   * Identifier of the compute resource
   * @return computeId
  **/
  @ApiModelProperty(required = true, value = "Identifier of the compute resource")
  public String getComputeId() {
    return computeId;
  }

  public void setComputeId(String computeId) {
    this.computeId = computeId;
  }

  public OperateComputeRequest computeOperation(String computeOperation) {
    this.computeOperation = computeOperation;
    return this;
  }

   /**
   * Operation Type on the compute resource
   * @return computeOperation
  **/
  @ApiModelProperty(required = true, value = "Operation Type on the compute resource")
  public String getComputeOperation() {
    return computeOperation;
  }

  public void setComputeOperation(String computeOperation) {
    this.computeOperation = computeOperation;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OperateComputeRequest operateComputeRequest = (OperateComputeRequest) o;
    return Objects.equals(this.computeId, operateComputeRequest.computeId) &&
        Objects.equals(this.computeOperation, operateComputeRequest.computeOperation);
  }

  @Override
  public int hashCode() {
    return Objects.hash(computeId, computeOperation);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OperateComputeRequest {\n");
    
    sb.append("    computeId: ").append(toIndentedString(computeId)).append("\n");
    sb.append("    computeOperation: ").append(toIndentedString(computeOperation)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
