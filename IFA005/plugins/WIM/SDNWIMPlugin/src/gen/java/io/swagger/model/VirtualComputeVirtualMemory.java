/*
 * WIM Manager API
 * WIM Manager API
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
import java.math.BigDecimal;
import javax.validation.constraints.*;

/**
 * The virtual memory of the compute.
 */
@ApiModel(description = "The virtual memory of the compute.")
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaJerseyServerCodegen", date = "2018-11-02T11:54:01.688+01:00")
public class VirtualComputeVirtualMemory   {
  @JsonProperty("virtualMemOversubscriptionPolicy")
  private String virtualMemOversubscriptionPolicy = null;

  @JsonProperty("numaEnabled")
  private Boolean numaEnabled = null;

  @JsonProperty("virtualMemSize")
  private BigDecimal virtualMemSize = null;

  public VirtualComputeVirtualMemory virtualMemOversubscriptionPolicy(String virtualMemOversubscriptionPolicy) {
    this.virtualMemOversubscriptionPolicy = virtualMemOversubscriptionPolicy;
    return this;
  }

  /**
   * The memory core oversubscription policy in terms of virtual memory to physical memory on the platform. The cardinality can be 0 if no policy has been defined during the allocation request.
   * @return virtualMemOversubscriptionPolicy
   **/
  @JsonProperty("virtualMemOversubscriptionPolicy")
  @ApiModelProperty(required = true, value = "The memory core oversubscription policy in terms of virtual memory to physical memory on the platform. The cardinality can be 0 if no policy has been defined during the allocation request.")
  @NotNull
  public String getVirtualMemOversubscriptionPolicy() {
    return virtualMemOversubscriptionPolicy;
  }

  public void setVirtualMemOversubscriptionPolicy(String virtualMemOversubscriptionPolicy) {
    this.virtualMemOversubscriptionPolicy = virtualMemOversubscriptionPolicy;
  }

  public VirtualComputeVirtualMemory numaEnabled(Boolean numaEnabled) {
    this.numaEnabled = numaEnabled;
    return this;
  }

  /**
   * It specifies the memory allocation to be cognisant of the relevant process/core allocation.
   * @return numaEnabled
   **/
  @JsonProperty("numaEnabled")
  @ApiModelProperty(required = true, value = "It specifies the memory allocation to be cognisant of the relevant process/core allocation.")
  @NotNull
  public Boolean isNumaEnabled() {
    return numaEnabled;
  }

  public void setNumaEnabled(Boolean numaEnabled) {
    this.numaEnabled = numaEnabled;
  }

  public VirtualComputeVirtualMemory virtualMemSize(BigDecimal virtualMemSize) {
    this.virtualMemSize = virtualMemSize;
    return this;
  }

  /**
   * Amount of virtual Memory (e.g. in MB).
   * @return virtualMemSize
   **/
  @JsonProperty("virtualMemSize")
  @ApiModelProperty(required = true, value = "Amount of virtual Memory (e.g. in MB).")
  @NotNull
  public BigDecimal getVirtualMemSize() {
    return virtualMemSize;
  }

  public void setVirtualMemSize(BigDecimal virtualMemSize) {
    this.virtualMemSize = virtualMemSize;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VirtualComputeVirtualMemory virtualComputeVirtualMemory = (VirtualComputeVirtualMemory) o;
    return Objects.equals(this.virtualMemOversubscriptionPolicy, virtualComputeVirtualMemory.virtualMemOversubscriptionPolicy) &&
        Objects.equals(this.numaEnabled, virtualComputeVirtualMemory.numaEnabled) &&
        Objects.equals(this.virtualMemSize, virtualComputeVirtualMemory.virtualMemSize);
  }

  @Override
  public int hashCode() {
    return Objects.hash(virtualMemOversubscriptionPolicy, numaEnabled, virtualMemSize);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VirtualComputeVirtualMemory {\n");
    
    sb.append("    virtualMemOversubscriptionPolicy: ").append(toIndentedString(virtualMemOversubscriptionPolicy)).append("\n");
    sb.append("    numaEnabled: ").append(toIndentedString(numaEnabled)).append("\n");
    sb.append("    virtualMemSize: ").append(toIndentedString(virtualMemSize)).append("\n");
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

