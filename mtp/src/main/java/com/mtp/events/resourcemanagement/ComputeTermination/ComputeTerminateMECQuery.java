/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mtp.events.resourcemanagement.ComputeTermination;

import java.util.List;

/**
 *
 * @author efabuba
 */
public class ComputeTerminateMECQuery {
    private long reqid;
    private long servid; //service identifiers
    private List<String> computereq; //contains vim computation info

    public ComputeTerminateMECQuery(long reqid, long servid, List<String> computereq) {
        this.reqid = reqid;
        this.servid = servid;
        this.computereq = computereq;
    }

    
    public long getReqid() {
        return reqid;
    }

    public void setReqid(long reqid) {
        this.reqid = reqid;
    }

    public long getServid() {
        return servid;
    }

    public void setServid(long servid) {
        this.servid = servid;
    }

    public List<String> getComputereq() {
        return computereq;
    }

    public void setComputereq(List<String> computereq) {
        this.computereq = computereq;
    }
    
    
}
