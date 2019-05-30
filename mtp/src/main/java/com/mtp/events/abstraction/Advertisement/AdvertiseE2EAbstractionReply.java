/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mtp.events.abstraction.Advertisement;

//import com.mtp.common.objects.VIME2EAbstractElem;
//import com.mtp.common.objects.WIME2EAbstractElem;
import com.mtp.extinterface.nbi.swagger.model.InlineResponse2003;

/**
 *
 * @author user
 */
public class AdvertiseE2EAbstractionReply {
    private long reqid;
    private InlineResponse2003 response;
    //private ArrayList<VIME2EAbstractElem> e2evimlist; //list of e2e vim resources
    //private ArrayList<WIME2EAbstractElem> e2ewimlist; //list of e2e wim resources

    public AdvertiseE2EAbstractionReply(long reqid, InlineResponse2003 response) {
        this.reqid = reqid;
        this.response = response;
    }

    public long getReqid() {
        return reqid;
    }

    public void setReqid(long reqid) {
        this.reqid = reqid;
    }

    public InlineResponse2003 getResponse() {
        return response;
    }

    public void setResponse(InlineResponse2003 response) {
        this.response = response;
    }
    
}
