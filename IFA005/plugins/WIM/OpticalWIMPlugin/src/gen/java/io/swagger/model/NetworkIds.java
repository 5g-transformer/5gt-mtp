/*
 * VIM Manager API
 * VIM Manager API
 *
 * OpenAPI spec version: 0.0.3
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package io.swagger.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import javax.validation.constraints.*;

/**
 * NetworkIds
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaJerseyServerCodegen", date = "2018-11-29T11:25:16.593Z")
public class NetworkIds   {
  @JsonProperty("networkId")
  private String networkId = null;

  public NetworkIds networkId(String networkId) {
    this.networkId = networkId;
    return this;
  }

  /**
   * Identifier of the virtualised network resource(s) to be terminated.
   * @return networkId
   **/
  @JsonProperty("networkId")
  @ApiModelProperty(required = true, value = "Identifier of the virtualised network resource(s) to be terminated.")
  @NotNull
  public String getNetworkId() {
    return networkId;
  }

  public void setNetworkId(String networkId) {
    this.networkId = networkId;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    NetworkIds networkIds = (NetworkIds) o;
    return Objects.equals(this.networkId, networkIds.networkId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(networkId);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class NetworkIds {\n");
    
    sb.append("    networkId: ").append(toIndentedString(networkId)).append("\n");
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
