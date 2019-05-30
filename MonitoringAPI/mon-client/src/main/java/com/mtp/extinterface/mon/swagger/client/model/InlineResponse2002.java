/*
 * Prometheus Manager API
 * The API of the Prometheus Manager.
 *
 * OpenAPI spec version: 0.1
 * Contact: m.capitani@nextworks.it
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package com.mtp.extinterface.mon.swagger.client.model;

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
import java.util.ArrayList;
import java.util.List;

/**
 * InlineResponse2002
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2019-05-06T07:52:18.537Z")
public class InlineResponse2002 {
  @SerializedName("deleted")
  private List<String> deleted = null;

  public InlineResponse2002 deleted(List<String> deleted) {
    this.deleted = deleted;
    return this;
  }

  public InlineResponse2002 addDeletedItem(String deletedItem) {
    if (this.deleted == null) {
      this.deleted = new ArrayList<String>();
    }
    this.deleted.add(deletedItem);
    return this;
  }

   /**
   * deleted dashboards
   * @return deleted
  **/
  @ApiModelProperty(value = "deleted dashboards")
  public List<String> getDeleted() {
    return deleted;
  }

  public void setDeleted(List<String> deleted) {
    this.deleted = deleted;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    InlineResponse2002 inlineResponse2002 = (InlineResponse2002) o;
    return Objects.equals(this.deleted, inlineResponse2002.deleted);
  }

  @Override
  public int hashCode() {
    return Objects.hash(deleted);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class InlineResponse2002 {\n");
    
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
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

