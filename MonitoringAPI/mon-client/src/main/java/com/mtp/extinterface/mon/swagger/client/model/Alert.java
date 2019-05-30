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

/**
 * Alert
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2019-05-06T07:52:18.537Z")
public class Alert {
  @SerializedName("alertId")
  private String alertId = null;

  @SerializedName("query")
  private String query = null;

  @SerializedName("label")
  private String label = null;

  /**
   * the severity of the alert
   */
  @JsonAdapter(SeverityEnum.Adapter.class)
  public enum SeverityEnum {
    WARNING("warning"),
    
    ERROR("error"),
    
    CRITICAL("critical");

    private String value;

    SeverityEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static SeverityEnum fromValue(String text) {
      for (SeverityEnum b : SeverityEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<SeverityEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final SeverityEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public SeverityEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return SeverityEnum.fromValue(String.valueOf(value));
      }
    }
  }

  @SerializedName("severity")
  private SeverityEnum severity = null;

  @SerializedName("value")
  private Double value = null;

  /**
   * the kind of inequality the query should satisfy related to the value
   */
  @JsonAdapter(KindEnum.Adapter.class)
  public enum KindEnum {
    G("g"),
    
    GEQ("geq"),
    
    L("l"),
    
    LEQ("leq"),
    
    EQ("eq"),
    
    NEQ("neq");

    private String value;

    KindEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static KindEnum fromValue(String text) {
      for (KindEnum b : KindEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<KindEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final KindEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public KindEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return KindEnum.fromValue(String.valueOf(value));
      }
    }
  }

  @SerializedName("kind")
  private KindEnum kind = null;

  @SerializedName("target")
  private String target = null;

  public Alert alertId(String alertId) {
    this.alertId = alertId;
    return this;
  }

   /**
   * the ID assigned to the alert
   * @return alertId
  **/
  @ApiModelProperty(value = "the ID assigned to the alert")
  public String getAlertId() {
    return alertId;
  }

  public void setAlertId(String alertId) {
    this.alertId = alertId;
  }

  public Alert query(String query) {
    this.query = query;
    return this;
  }

   /**
   * the query whose value should be monitored. See https://prometheus.io/docs/prometheus/latest/querying/basics/ for details 
   * @return query
  **/
  @ApiModelProperty(value = "the query whose value should be monitored. See https://prometheus.io/docs/prometheus/latest/querying/basics/ for details ")
  public String getQuery() {
    return query;
  }

  public void setQuery(String query) {
    this.query = query;
  }

  public Alert label(String label) {
    this.label = label;
    return this;
  }

   /**
   * the label that will be used in the notifications
   * @return label
  **/
  @ApiModelProperty(value = "the label that will be used in the notifications")
  public String getLabel() {
    return label;
  }

  public void setLabel(String label) {
    this.label = label;
  }

  public Alert severity(SeverityEnum severity) {
    this.severity = severity;
    return this;
  }

   /**
   * the severity of the alert
   * @return severity
  **/
  @ApiModelProperty(value = "the severity of the alert")
  public SeverityEnum getSeverity() {
    return severity;
  }

  public void setSeverity(SeverityEnum severity) {
    this.severity = severity;
  }

  public Alert value(Double value) {
    this.value = value;
    return this;
  }

   /**
   * the value associated to the threshold
   * @return value
  **/
  @ApiModelProperty(value = "the value associated to the threshold")
  public Double getValue() {
    return value;
  }

  public void setValue(Double value) {
    this.value = value;
  }

  public Alert kind(KindEnum kind) {
    this.kind = kind;
    return this;
  }

   /**
   * the kind of inequality the query should satisfy related to the value
   * @return kind
  **/
  @ApiModelProperty(value = "the kind of inequality the query should satisfy related to the value")
  public KindEnum getKind() {
    return kind;
  }

  public void setKind(KindEnum kind) {
    this.kind = kind;
  }

  public Alert target(String target) {
    this.target = target;
    return this;
  }

   /**
   * Get target
   * @return target
  **/
  @ApiModelProperty(value = "")
  public String getTarget() {
    return target;
  }

  public void setTarget(String target) {
    this.target = target;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Alert alert = (Alert) o;
    return Objects.equals(this.alertId, alert.alertId) &&
        Objects.equals(this.query, alert.query) &&
        Objects.equals(this.label, alert.label) &&
        Objects.equals(this.severity, alert.severity) &&
        Objects.equals(this.value, alert.value) &&
        Objects.equals(this.kind, alert.kind) &&
        Objects.equals(this.target, alert.target);
  }

  @Override
  public int hashCode() {
    return Objects.hash(alertId, query, label, severity, value, kind, target);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Alert {\n");
    
    sb.append("    alertId: ").append(toIndentedString(alertId)).append("\n");
    sb.append("    query: ").append(toIndentedString(query)).append("\n");
    sb.append("    label: ").append(toIndentedString(label)).append("\n");
    sb.append("    severity: ").append(toIndentedString(severity)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
    sb.append("    kind: ").append(toIndentedString(kind)).append("\n");
    sb.append("    target: ").append(toIndentedString(target)).append("\n");
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

